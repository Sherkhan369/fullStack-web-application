'use client';

import { type ReactNode, useState } from 'react';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

// [Task]: T039a
// [From]: specs/001-fullstack-todo-auth/spec.md FR-013 (responsive UX) + FR-007 (task interactions)

export default function Providers({ children }: { children: ReactNode }) {
  const [queryClient] = useState(() => new QueryClient());

  return <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>;
}
