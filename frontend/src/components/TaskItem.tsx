'use client';

import { useState } from 'react';
import { Task } from '@/types/task';
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { apiService } from '@/services/api';

interface TaskItemProps {
  task: Task;
  onDelete: () => void;
  onToggle: () => void;
  isLoading?: boolean;
}

export default function TaskItem({ task, onDelete, onToggle, isLoading = false }: TaskItemProps) {
  const [isEditing, setIsEditing] = useState(false);
  const [editData, setEditData] = useState({
    title: task.title,
    description: task.description || '',
  });

  const queryClient = useQueryClient();

  const updateTaskMutation = useMutation({
    mutationFn: (updateData: Partial<Task>) => apiService.updateTask(task.id, updateData),
    onSuccess: (updatedTask) => {
      queryClient.setQueryData(['tasks'], (oldTasks: Task[] = []) =>
        oldTasks.map(t => t.id === updatedTask.id ? updatedTask : t)
      );
      setIsEditing(false);
    },
  });

  const handleEditSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!editData.title.trim()) return;

    updateTaskMutation.mutate({
      title: editData.title,
      description: editData.description,
    });
  };

  const handleToggle = () => {
    if (!isLoading) {
      onToggle();
    }
  };

  const handleDelete = () => {
    if (!isLoading && confirm('Are you sure you want to delete this task?')) {
      onDelete();
    }
  };

  return (
    <div
      className={`rounded-xl p-5 transition-all duration-300 ${
        task.is_complete
          ? 'bg-gradient-to-r from-green-50 to-emerald-50 dark:from-green-900/20 dark:to-emerald-900/20 border border-green-200 dark:border-green-800/50'
          : 'bg-gradient-to-r from-white to-gray-50 dark:from-gray-800 dark:to-gray-800/50 border border-gray-200 dark:border-gray-700'
      } shadow-sm hover:shadow-md`}
      role="article"
      aria-label={`Task: ${task.title}`}
    >
      {isEditing ? (
        <form onSubmit={handleEditSubmit} className="space-y-4">
          <div>
            <label htmlFor={`task-title-${task.id}`} className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
              Task Title
            </label>
            <input
              id={`task-title-${task.id}`}
              type="text"
              value={editData.title}
              onChange={(e) => setEditData({ ...editData, title: e.target.value })}
              className="w-full px-4 py-2.5 rounded-lg border border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white transition duration-200"
              autoFocus
              aria-label="Edit task title"
            />
          </div>
          <div>
            <label htmlFor={`task-desc-${task.id}`} className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1">
              Task Description
            </label>
            <textarea
              id={`task-desc-${task.id}`}
              value={editData.description}
              onChange={(e) => setEditData({ ...editData, description: e.target.value })}
              rows={3}
              className="w-full px-4 py-2.5 rounded-lg border border-gray-300 dark:border-gray-600 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white transition duration-200"
              placeholder="Description (optional)"
              aria-label="Edit task description"
            />
          </div>
          <div className="flex justify-end space-x-3 pt-2">
            <button
              type="button"
              onClick={() => {
                setIsEditing(false);
                setEditData({ title: task.title, description: task.description || '' });
              }}
              className="px-4 py-2 text-sm font-medium text-gray-700 dark:text-gray-300 bg-gray-100 dark:bg-gray-700 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-lg transition-colors duration-200"
              aria-label="Cancel editing"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={updateTaskMutation.isPending}
              className="px-4 py-2 text-sm font-medium text-white bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 rounded-lg shadow transition-all duration-200 disabled:opacity-50"
              aria-label="Save changes"
            >
              {updateTaskMutation.isPending ? (
                <span className="flex items-center">
                  <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Saving...
                </span>
              ) : 'Save'}
            </button>
          </div>
        </form>
      ) : (
        <div className="space-y-3">
          <div className="flex items-start justify-between">
            <div className="flex items-start space-x-4 flex-1">
              <button
                onClick={handleToggle}
                disabled={isLoading}
                className={`flex-shrink-0 w-6 h-6 rounded-full border-2 transition-all duration-200 flex items-center justify-center ${
                  task.is_complete
                    ? 'bg-gradient-to-r from-green-500 to-emerald-500 border-green-500 shadow-inner'
                    : 'border-gray-400 dark:border-gray-500 hover:border-green-500 hover:shadow-md'
                }`}
                aria-label={task.is_complete ? 'Mark as incomplete' : 'Mark as complete'}
                aria-checked={task.is_complete}
                role="checkbox"
              >
                {task.is_complete && (
                  <svg className="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
                    <path fillRule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clipRule="evenodd" />
                  </svg>
                )}
              </button>
              <div className="flex-1">
                <h3
                  className={`text-lg font-semibold ${
                    task.is_complete
                      ? 'text-gray-500 dark:text-gray-400 line-through'
                      : 'text-gray-900 dark:text-white'
                  }`}
                  id={`task-title-${task.id}`}
                >
                  {task.title}
                </h3>
                {task.description && (
                  <p
                    className={`mt-1 text-gray-600 dark:text-gray-400 ${
                      task.is_complete ? 'line-through' : ''
                    }`}
                    id={`task-desc-${task.id}`}
                  >
                    {task.description}
                  </p>
                )}
              </div>
            </div>

            <div className="flex items-center space-x-2">
              <time
                dateTime={task.created_at}
                className="text-xs text-gray-500 dark:text-gray-400 font-medium"
                aria-label={`Created on ${new Date(task.created_at).toLocaleDateString()}`}
              >
                {new Date(task.created_at).toLocaleDateString()}
              </time>
              <button
                onClick={() => setIsEditing(true)}
                disabled={isLoading}
                className="p-2 text-gray-500 hover:text-gray-700 dark:hover:text-gray-200 transition-colors rounded-lg hover:bg-gray-100 dark:hover:bg-gray-700 min-w-[36px] min-h-[36px] flex items-center justify-center"
                aria-label="Edit task"
                aria-describedby={`task-title-${task.id}`}
              >
                <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
                  <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
                </svg>
              </button>
              <button
                onClick={handleDelete}
                disabled={isLoading}
                className="p-2 text-red-500 hover:text-red-600 dark:hover:text-red-400 transition-colors rounded-lg hover:bg-red-50 dark:hover:bg-red-900/20 min-w-[36px] min-h-[36px] flex items-center justify-center"
                aria-label="Delete task"
                aria-describedby={`task-title-${task.id}`}
              >
                <svg className="w-4 h-4" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true">
                  <path fillRule="evenodd" d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9zM4 5a2 2 0 012-2h8a2 2 0 012 2v6a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm3 4a1 1 0 102 0v-1a1 1 0 10-2 0v1zm4 0a1 1 0 102 0v-1a1 1 0 10-2 0v1z" clipRule="evenodd" />
                </svg>
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}