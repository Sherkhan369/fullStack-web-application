import { CreateTaskData, Task, User, AuthResponse } from '@/types';

// [Task]: T039a, T047
// [From]: specs/001-fullstack-todo-auth/spec.md FR-004, FR-007 (task creation/edit flows), FR-016 (error handling)

const API_BASE_URL = process.env.NEXT_PUBLIC_API_BASE_URL || 'http://localhost:8000';

class ApiService {
  private getToken(): string | null {
    if (typeof window !== 'undefined') {
      return localStorage.getItem('access_token');
    }
    return null;
  }

  private getAuthHeaders(): HeadersInit {
    const token = this.getToken();
    return {
      'Content-Type': 'application/json',
      ...(token && { 'Authorization': `Bearer ${token}` }),
    };
  }

  private async handleResponse<T>(response: Response): Promise<T> {
    if (!response.ok) {
      const errorBody = await response.text();
      let errorData: any;

      try {
        errorData = JSON.parse(errorBody);
      } catch {
        // If response is not JSON, create a generic error
        errorData = {
          error: 'Request Error',
          message: `HTTP ${response.status}: ${response.statusText}`,
          status_code: response.status
        };
      }

      // Throw a more detailed error
      throw new Error(errorData.detail || errorData.message || `HTTP ${response.status}: Request failed`);
    }

    // Handle empty response for DELETE requests
    if (response.status === 204) {
      return undefined as unknown as T;
    }

    return response.json();
  }

  // Task API methods
  async getTasks(): Promise<Task[]> {
    const response = await fetch(`${API_BASE_URL}/api/v1/tasks`, {
      method: 'GET',
      headers: this.getAuthHeaders(),
    });

    return this.handleResponse<Task[]>(response);
  }

  async createTask(taskData: CreateTaskData): Promise<Task> {
    const response = await fetch(`${API_BASE_URL}/api/v1/tasks`, {
      method: 'POST',
      headers: this.getAuthHeaders(),
      body: JSON.stringify(taskData),
    });

    return this.handleResponse<Task>(response);
  }

  async updateTask(taskId: string, taskData: Partial<Task>): Promise<Task> {
    const response = await fetch(`${API_BASE_URL}/api/v1/tasks/${taskId}`, {
      method: 'PUT',
      headers: this.getAuthHeaders(),
      body: JSON.stringify(taskData),
    });

    return this.handleResponse<Task>(response);
  }

  async deleteTask(taskId: string): Promise<void> {
    const response = await fetch(`${API_BASE_URL}/api/v1/tasks/${taskId}`, {
      method: 'DELETE',
      headers: this.getAuthHeaders(),
    });

    return this.handleResponse<void>(response);
  }

  async toggleTaskCompletion(taskId: string): Promise<Task> {
    const response = await fetch(`${API_BASE_URL}/api/v1/tasks/${taskId}/toggle`, {
      method: 'PATCH',
      headers: this.getAuthHeaders(),
    });

    return this.handleResponse<Task>(response);
  }

  // User API methods
  async getCurrentUser(): Promise<User> {
    const response = await fetch(`${API_BASE_URL}/api/v1/auth/me`, {
      method: 'GET',
      headers: this.getAuthHeaders(),
    });

    return this.handleResponse<User>(response);
  }

  async getTaskStatistics(): Promise<any> {
    const response = await fetch(`${API_BASE_URL}/api/v1/tasks/statistics`, {
      method: 'GET',
      headers: this.getAuthHeaders(),
    });

    return this.handleResponse<any>(response);
  }
}

export const apiService = new ApiService();