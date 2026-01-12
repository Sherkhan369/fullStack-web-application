// User-related type definitions

export interface User {
  id: string;
  email: string;
  created_at: string;
  updated_at: string;
  is_active: boolean;
}

export interface UserLoginData {
  email: string;
  password: string;
}

export interface UserRegistrationData {
  email: string;
  password: string;
}

export interface AuthToken {
  access_token: string;
  refresh_token?: string;
  token_type: string;
}

export interface AuthResponse {
  user: User;
  access_token: string;
  refresh_token?: string;
  token_type: string;
}