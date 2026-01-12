'use client';

import React, { Component, ErrorInfo, ReactNode } from 'react';
import { AlertCircle, RefreshCw } from 'lucide-react';
import Link from 'next/link';

interface Props {
  children: ReactNode;
}

interface State {
  hasError: boolean;
  error?: Error;
  errorInfo?: ErrorInfo;
}

export default class ErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error: Error): State {
    // Update state so the next render will show the fallback UI
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    // Log error details
    this.setState({
      error,
      errorInfo,
    });

    // In a real application, you would send this to an error reporting service
    console.error('Error caught by boundary:', error, errorInfo);
  }

  handleRetry = () => {
    this.setState({ hasError: false, error: undefined, errorInfo: undefined });
  };

  render() {
    if (this.state.hasError) {
      // Check if it's an authentication error
      const isAuthError = this.state.error?.message?.includes('401') ||
                         this.state.error?.message?.includes('Unauthorized') ||
                         this.state.error?.message?.includes('authentication');

      if (isAuthError) {
        return (
          <div className="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900">
            <div className="max-w-md w-full bg-white dark:bg-gray-800 shadow-lg rounded-lg p-6">
              <div className="flex items-center justify-center w-12 h-12 mx-auto bg-red-100 dark:bg-red-900/20 rounded-full">
                <AlertCircle className="w-6 h-6 text-red-600 dark:text-red-400" />
              </div>

              <div className="mt-4 text-center">
                <h2 className="text-lg font-semibold text-gray-900 dark:text-white">
                  Authentication Required
                </h2>
                <p className="mt-2 text-gray-600 dark:text-gray-300">
                  Your session has expired or you don't have permission to access this resource.
                </p>

                <div className="mt-6 space-y-3">
                  <Link
                    href="/login"
                    className="block w-full bg-blue-600 hover:bg-blue-700 text-white text-center py-2 px-4 rounded-md transition-colors duration-200"
                  >
                    Sign In
                  </Link>
                  <Link
                    href="/"
                    className="block w-full text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white text-center py-2 px-4 rounded-md transition-colors duration-200"
                  >
                    Go Home
                  </Link>
                </div>
              </div>
            </div>
          </div>
        );
      }

      // Generic error fallback
      return (
        <div className="min-h-screen flex items-center justify-center bg-gray-50 dark:bg-gray-900">
          <div className="max-w-md w-full bg-white dark:bg-gray-800 shadow-lg rounded-lg p-6">
            <div className="flex items-center justify-center w-12 h-12 mx-auto bg-red-100 dark:bg-red-900/20 rounded-full">
              <AlertCircle className="w-6 h-6 text-red-600 dark:text-red-400" />
            </div>

            <div className="mt-4 text-center">
              <h2 className="text-lg font-semibold text-gray-900 dark:text-white">
                Something went wrong
              </h2>
              <p className="mt-2 text-gray-600 dark:text-gray-300">
                An unexpected error occurred. Please try again.
              </p>

              <div className="mt-6 space-y-3">
                <button
                  onClick={this.handleRetry}
                  className="flex items-center justify-center w-full bg-blue-600 hover:bg-blue-700 text-white py-2 px-4 rounded-md transition-colors duration-200"
                >
                  <RefreshCw className="w-4 h-4 mr-2" />
                  Try Again
                </button>
                <Link
                  href="/"
                  className="block w-full text-gray-600 dark:text-gray-300 hover:text-gray-900 dark:hover:text-white text-center py-2 px-4 rounded-md transition-colors duration-200"
                >
                  Go Home
                </Link>
              </div>

              {process.env.NODE_ENV === 'development' && this.state.error && (
                <details className="mt-4">
                  <summary className="cursor-pointer text-sm text-gray-500 dark:text-gray-400">
                    Error Details (Development)
                  </summary>
                  <pre className="mt-2 text-xs text-gray-600 dark:text-gray-300 bg-gray-100 dark:bg-gray-700 p-2 rounded overflow-auto max-h-32">
                    {this.state.error.toString()}
                    {this.state.errorInfo?.componentStack}
                  </pre>
                </details>
              )}
            </div>
          </div>
        </div>
      );
    }

    return this.props.children;
  }
}