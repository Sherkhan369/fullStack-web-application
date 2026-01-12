'use client';

import { Task } from '@/types/task';
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { apiService } from '@/services/api';
import TaskItem from './TaskItem';
import SwipeableTaskItem from './SwipeableTaskItem';
import SkeletonTaskItem from './SkeletonTaskItem';
import Link from 'next/link';

interface TaskListProps {
  tasks: Task[];
  isLoading?: boolean;
}

export default function TaskList({ tasks, isLoading = false }: TaskListProps) {
  const queryClient = useQueryClient();

  // Delete task mutation
  const deleteMutation = useMutation({
    mutationFn: (taskId: string) => apiService.deleteTask(taskId),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['tasks'] });
    },
  });

  // Toggle completion mutation
  const toggleMutation = useMutation({
    mutationFn: (taskId: string) => apiService.toggleTaskCompletion(taskId),
    onSuccess: (updatedTask) => {
      queryClient.setQueryData(['tasks'], (oldTasks: Task[] = []) =>
        oldTasks.map(task =>
          task.id === updatedTask.id ? updatedTask : task
        )
      );
    },
  });

  if (isLoading) {
    // Show skeleton screens when loading
    return (
      <div className="space-y-5">
        {[...Array(3)].map((_, index) => (
          <SkeletonTaskItem key={`skeleton-${index}`} />
        ))}
      </div>
    );
  }

  if (tasks.length === 0) {
    return (
      <div className="text-center py-12">
        <div className="mx-auto w-24 h-24 bg-gradient-to-br from-gray-100 to-gray-200 dark:from-gray-700 dark:to-gray-800 rounded-full flex items-center justify-center mb-6">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 text-gray-400 dark:text-gray-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
          </svg>
        </div>
        <h3 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">
          No tasks yet
        </h3>
        <p className="text-gray-600 dark:text-gray-400 mb-6 max-w-md mx-auto">
          Get started by creating your first task. You'll be able to track your progress and stay organized.
        </p>
        <Link
          href="/dashboard/tasks/new"
          className="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-600 to-indigo-600 text-white font-semibold rounded-xl shadow-lg hover:from-blue-700 hover:to-indigo-700 transition-all duration-300 transform hover:-translate-y-0.5 hover:shadow-xl"
        >
          Create your first task
          <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5 ml-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
          </svg>
        </Link>
      </div>
    );
  }

  return (
    <div className="space-y-4">
      {tasks.map((task) => (
        <SwipeableTaskItem
          key={task.id}
          task={task}
          onDelete={() => deleteMutation.mutate(task.id)}
          onToggle={() => toggleMutation.mutate(task.id)}
          isLoading={deleteMutation.isPending || toggleMutation.isPending}
        />
      ))}
    </div>
  );
}