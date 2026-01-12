'use client';

import { useState, useRef, useEffect } from 'react';
import { Task } from '@/types/task';
import TaskItem from './TaskItem';

interface SwipeableTaskItemProps {
  task: Task;
  onDelete: () => void;
  onToggle: () => void;
  isLoading?: boolean;
}

export default function SwipeableTaskItem({ task, onDelete, onToggle, isLoading = false }: SwipeableTaskItemProps) {
  const [startX, setStartX] = useState(0);
  const [currentX, setCurrentX] = useState(0);
  const [isSwiping, setIsSwiping] = useState(false);
  const [isSwiped, setIsSwiped] = useState(false);
  const elementRef = useRef<HTMLDivElement>(null);

  const handleTouchStart = (e: React.TouchEvent) => {
    setStartX(e.touches[0].clientX);
    setIsSwiping(true);
  };

  const handleTouchMove = (e: React.TouchEvent) => {
    if (!isSwiping) return;

    const currentXPos = e.touches[0].clientX;
    setCurrentX(currentXPos);

    // Calculate the difference
    const diff = startX - currentXPos;

    // Only allow swiping to the left (for completion)
    if (diff > 0) {
      // Apply a transform that increases as swipe progresses
      const translateX = Math.min(diff, 75); // Limit to 75px
      if (elementRef.current) {
        elementRef.current.style.transform = `translateX(-${translateX}px)`;
        // Show swipe hint when swiping past threshold
        const swipeHint = elementRef.current.querySelector('.swipe-hint');
        if (swipeHint) {
          const opacity = Math.min((diff - 10) / 40, 1); // Start showing hint after 10px, fully visible at 50px
          (swipeHint as HTMLElement).style.opacity = opacity.toString();
        }
      }
    }
  };

  const handleTouchEnd = () => {
    if (!isSwiping) return;

    const diff = startX - currentX;

    // If swipe is more than 50px, consider it a completion swipe
    if (diff > 50 && !task.is_complete) {
      setIsSwiped(true);
      setTimeout(() => {
        onToggle();
        resetSwipe();
      }, 300);
    } else {
      // Reset the position
      resetSwipe();
    }

    setIsSwiping(false);
  };

  const resetSwipe = () => {
    if (elementRef.current) {
      elementRef.current.style.transform = 'translateX(0)';
      // Reset swipe hint opacity
      const swipeHint = elementRef.current.querySelector('.swipe-hint');
      if (swipeHint) {
        (swipeHint as HTMLElement).style.opacity = '0';
      }
    }
    setIsSwiping(false);
    setIsSwiped(false);
    setCurrentX(0);
  };

  // Handle mouse events for testing on desktop
  const handleMouseDown = (e: React.MouseEvent) => {
    setStartX(e.clientX);
    setIsSwiping(true);
  };

  const handleMouseMove = (e: React.MouseEvent) => {
    if (!isSwiping) return;

    const currentXPos = e.clientX;
    setCurrentX(currentXPos);

    const diff = startX - currentXPos;

    if (diff > 0) {
      const translateX = Math.min(diff, 75);
      if (elementRef.current) {
        elementRef.current.style.transform = `translateX(-${translateX}px)`;
        // Show swipe hint when swiping past threshold
        const swipeHint = elementRef.current.querySelector('.swipe-hint');
        if (swipeHint) {
          const opacity = Math.min((diff - 10) / 40, 1);
          (swipeHint as HTMLElement).style.opacity = opacity.toString();
        }
      }
    }
  };

  const handleMouseUp = () => {
    if (!isSwiping) return;

    const diff = startX - currentX;

    if (diff > 50 && !task.is_complete) {
      setIsSwiped(true);
      setTimeout(() => {
        onToggle();
        resetSwipe();
      }, 300);
    } else {
      resetSwipe();
    }

    setIsSwiping(false);
  };

  // Add mouse up listener to document when swiping starts
  useEffect(() => {
    if (isSwiping) {
      const handleGlobalMouseUp = () => {
        if (isSwiping) {
          handleMouseUp();
        }
      };

      const handleGlobalMouseMove = (e: MouseEvent) => {
        if (isSwiping) {
          // Create a synthetic event to match React.MouseEvent
          const syntheticEvent = {
            ...e,
            nativeEvent: e,
            currentTarget: e.currentTarget as EventTarget & HTMLDivElement,
            target: e.target as EventTarget,
            bubbles: e.bubbles,
            cancelable: e.cancelable,
            defaultPrevented: e.defaultPrevented,
            eventPhase: e.eventPhase,
            isTrusted: e.isTrusted,
            preventDefault: () => e.preventDefault(),
            isDefaultPrevented: () => e.defaultPrevented,
            stopPropagation: () => e.stopPropagation(),
            isPropagationStopped: () => false,
            persist: () => {},
            timeStamp: e.timeStamp,
            type: e.type,
          } as unknown as React.MouseEvent;

          handleMouseMove(syntheticEvent);
        }
      };

      document.addEventListener('mouseup', handleGlobalMouseUp);
      document.addEventListener('mousemove', handleGlobalMouseMove);

      return () => {
        document.removeEventListener('mouseup', handleGlobalMouseUp);
        document.removeEventListener('mousemove', handleGlobalMouseMove);
      };
    }
  }, [isSwiping, handleMouseMove]);

  return (
    <div
      ref={elementRef}
      className={`relative overflow-hidden rounded-lg transition-all duration-200 ease-out ${isSwiped ? 'opacity-0 scale-95' : 'opacity-100'} ${task.is_complete ? 'bg-gray-50 dark:bg-gray-800/50' : 'bg-white dark:bg-gray-800'}`}
      onTouchStart={handleTouchStart}
      onTouchMove={handleTouchMove}
      onTouchEnd={handleTouchEnd}
      onMouseDown={handleMouseDown}
      style={{
        touchAction: 'pan-y',
      }}
      aria-label={`Swipeable task: ${task.title}`}
    >
      {/* Swipe hint for completion */}
      {!task.is_complete && (
        <div
          className="swipe-hint absolute inset-y-0 right-0 w-16 bg-green-500 text-white flex items-center justify-center rounded-r-lg opacity-0 transition-opacity duration-200 z-0"
          aria-hidden="true"
        >
          <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M5 13l4 4L19 7" />
          </svg>
        </div>
      )}

      {/* Task content */}
      <div className="relative z-10">
        <TaskItem
          task={task}
          onDelete={onDelete}
          onToggle={onToggle}
          isLoading={isLoading}
        />
      </div>
    </div>
  );
}