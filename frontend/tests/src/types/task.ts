export interface Task {
  id: string;
  title: string;
  description?: string;
  is_complete: boolean;
  created_at: string;
  updated_at: string;
  user_id: string;
}

export interface CreateTaskData {
  title: string;
  description?: string;
}

export interface UpdateTaskData {
  title?: string;
  description?: string;
  is_complete?: boolean;
}