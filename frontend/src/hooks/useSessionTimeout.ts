'use client';

import { useEffect, useRef, useCallback } from 'react';

// [Task]: T039a
// [From]: specs/001-fullstack-todo-auth/spec.md FR-013 (supports responsive UX by enforcing session rules)
import { useAuth } from '@/lib/auth';

/**
 * Hook for handling session timeout and user activity tracking.
 *
 * @param timeoutMinutes - Session timeout in minutes (default: 30)
 * @param warningMinutes - Warning time before timeout in minutes (default: 5)
 */
export function useSessionTimeout(timeoutMinutes: number = 30, warningMinutes: number = 5) {
  const { logout } = useAuth();
  const lastActivityRef = useRef<number>(Date.now());
  const warningTimerRef = useRef<NodeJS.Timeout | null>(null);
  const timeoutTimerRef = useRef<NodeJS.Timeout | null>(null);
  const warningShownRef = useRef<boolean>(false);

  const resetActivity = useCallback(() => {
    lastActivityRef.current = Date.now();
    warningShownRef.current = false;

    // Clear existing timers
    if (warningTimerRef.current) {
      clearTimeout(warningTimerRef.current);
    }
    if (timeoutTimerRef.current) {
      clearTimeout(timeoutTimerRef.current);
    }

    // Set new timers
    const warningTime = (timeoutMinutes - warningMinutes) * 60 * 1000;
    const totalTime = timeoutMinutes * 60 * 1000;

    warningTimerRef.current = setTimeout(() => {
      if (!warningShownRef.current) {
        warningShownRef.current = true;
        showWarning(timeoutMinutes, warningMinutes);
      }
    }, warningTime);

    timeoutTimerRef.current = setTimeout(() => {
      handleTimeout();
    }, totalTime);
  }, [timeoutMinutes, warningMinutes]);

  const showWarning = useCallback((totalMinutes: number, warningMinutes: number) => {
    const warningTime = warningMinutes * 60 * 1000;
    const warning = `Your session will expire in ${warningMinutes} minutes due to inactivity. Click OK to continue your session.`;

    if (confirm(warning)) {
      resetActivity();
    } else {
      handleTimeout();
    }
  }, [resetActivity]);

  const handleTimeout = useCallback(() => {
    // Show final warning before logout
    alert('Your session has expired due to inactivity. You will be logged out.');
    logout.mutate();
  }, [logout]);

  useEffect(() => {
    // Initialize timers
    resetActivity();

    // Activity tracking events
    const events = ['mousedown', 'mousemove', 'keypress', 'scroll', 'touchstart'];

    const handleActivity = () => {
      resetActivity();
    };

    // Add event listeners
    events.forEach(event => {
      document.addEventListener(event, handleActivity, { passive: true });
    });

    // Cleanup function
    return () => {
      // Clear timers
      if (warningTimerRef.current) {
        clearTimeout(warningTimerRef.current);
      }
      if (timeoutTimerRef.current) {
        clearTimeout(timeoutTimerRef.current);
      }

      // Remove event listeners
      events.forEach(event => {
        document.removeEventListener(event, handleActivity);
      });
    };
  }, [resetActivity]);

  return {
    lastActivity: lastActivityRef.current,
    resetActivity,
  };
}