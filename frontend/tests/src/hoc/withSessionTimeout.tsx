'use client';

import { ReactNode, useEffect } from 'react';
import { useSessionTimeout } from '@/hooks/useSessionTimeout';
import { useAuth } from '@/lib/auth';

interface WithSessionTimeoutProps {
  children: ReactNode;
  timeoutMinutes?: number;
  warningMinutes?: number;
}

/**
 * Higher-order component that adds session timeout functionality to pages.
 */
export default function withSessionTimeout<P extends object>(
  WrappedComponent: React.ComponentType<P>,
  timeoutMinutes: number = 30,
  warningMinutes: number = 5
) {
  return function WithSessionTimeout(props: P) {
    const { children } = props as any;
    const { resetActivity } = useSessionTimeout(timeoutMinutes, warningMinutes);
    const { auth } = useAuth();

    // Reset activity when component mounts or user changes
    useEffect(() => {
      if (auth?.user) {
        resetActivity();
      }
    }, [auth?.user, resetActivity]);

    return (
      <div>
        {children || <WrappedComponent {...props} />}
      </div>
    );
  };
}