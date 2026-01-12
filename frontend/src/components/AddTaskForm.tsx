'use client';

import { useState } from 'react';
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { CreateTaskData, Task } from '@/types/task';
import { apiService } from '@/services/api';

// [Task]: T039a
// [From]: specs/001-fullstack-todo-auth/spec.md FR-004, FR-007 (task creation/edit flows)

interface AddTaskFormProps {
  onSuccess?: () => void;
}

export default function AddTaskForm({ onSuccess }: AddTaskFormProps) {
  const [formData, setFormData] = useState({
    title: '',
    description: '',
  });
  const [isExpanded, setIsExpanded] = useState(false);

  const queryClient = useQueryClient();

  const createTaskMutation = useMutation({
    mutationFn: (taskData: CreateTaskData) => apiService.createTask(taskData),
    onSuccess: () => {
      setFormData({ title: '', description: '' });
      setIsExpanded(false);
      queryClient.invalidateQueries({ queryKey: ['tasks'] });
      onSuccess?.();
    },
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();

    if (!formData.title.trim()) {
      return;
    }

    createTaskMutation.mutate({
      title: formData.title,
      description: formData.description,
    });
  };

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  if (isExpanded) {
    return (
      <div className="bg-gradient-to-br from-white to-gray-50 dark:from-gray-800 dark:to-gray-800/50 rounded-2xl shadow-lg border border-gray-200 dark:border-gray-700 p-6 mb-6">
        <form onSubmit={handleSubmit} className="space-y-5" role="form" aria-label="Add new task form">
          <div>
            <label htmlFor="title" className="block text-sm font-semibold text-gray-700 dark:text-gray-300 mb-2">
              Task Title
            </label>
            <input
              type="text"
              id="title"
              name="title"
              value={formData.title}
              onChange={handleInputChange}
              className="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white transition duration-200"
              placeholder="Enter task title"
              required
              aria-required="true"
              aria-describedby="title-error"
            />
            <div id="title-error" className="sr-only" role="alert"></div>
          </div>

          <div>
            <label htmlFor="description" className="block text-sm font-semibold text-gray-700 dark:text-gray-300 mb-2">
              Description (Optional)
            </label>
            <textarea
              id="description"
              name="description"
              value={formData.description}
              onChange={handleInputChange}
              rows={3}
              className="w-full px-4 py-3 border border-gray-300 dark:border-gray-600 rounded-xl shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white transition duration-200"
              placeholder="Enter task description"
              aria-describedby="desc-help"
            />
            <p id="desc-help" className="sr-only">Optional task description</p>
          </div>

          <div className="flex justify-end space-x-3 pt-2">
            <button
              type="button"
              onClick={() => {
                setIsExpanded(false);
                setFormData({ title: '', description: '' });
              }}
              className="px-4 py-2.5 text-sm font-medium text-gray-700 dark:text-gray-300 bg-gray-100 dark:bg-gray-700 hover:bg-gray-200 dark:hover:bg-gray-600 rounded-lg transition-colors duration-200"
            >
              Cancel
            </button>
            <button
              type="submit"
              disabled={createTaskMutation.isPending}
              className="px-4 py-2.5 text-sm font-medium text-white bg-gradient-to-r from-blue-600 to-indigo-600 hover:from-blue-700 hover:to-indigo-700 rounded-lg shadow transition-all duration-200 disabled:opacity-50"
            >
              {createTaskMutation.isPending ? (
                <span className="flex items-center">
                  <svg className="animate-spin -ml-1 mr-2 h-4 w-4 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                  </svg>
                  Creating...
                </span>
              ) : 'Create Task'}
            </button>
          </div>
        </form>
      </div>
    );
  }

  return (
    <div className="mb-6">
      <button
        onClick={() => setIsExpanded(true)}
        className="w-full bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-800 dark:to-gray-800/50 hover:from-gray-100 hover:to-gray-200 dark:hover:from-gray-700 dark:hover:to-gray-700/50 border-2 border-dashed border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 rounded-2xl py-6 px-6 transition-all duration-300 hover:shadow-md min-h-[80px]"
        aria-label="Add new task"
      >
        <div className="flex items-center justify-center space-x-3">
          <div className="w-10 h-10 bg-gradient-to-r from-blue-500 to-indigo-500 rounded-full flex items-center justify-center text-white font-bold">
            +
          </div>
          <span className="text-lg font-medium">Add New Task</span>
        </div>
      </button>
    </div>
  );
}