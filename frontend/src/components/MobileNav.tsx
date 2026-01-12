'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { Menu, X, LayoutDashboard, ListTodo, PlusCircle, LogOut } from 'lucide-react';

import { cn } from '@/styles/responsive';
import { useAuth } from '@/lib/auth';

// [Task]: T040
// [From]: specs/001-fullstack-todo-auth/spec.md FR-013 (responsive UI) + FR-014 (navigation)

export default function MobileNav() {
  const pathname = usePathname();
  const { auth, logout } = useAuth();

  const [open, setOpen] = useState(false);

  useEffect(() => {
    // Close the drawer when route changes
    setOpen(false);
  }, [pathname]);

  const navItems = [
    {
      href: '/dashboard',
      label: 'Dashboard',
      icon: LayoutDashboard,
    },
    {
      href: '/dashboard/tasks',
      label: 'Tasks',
      icon: ListTodo,
    },
    {
      href: '/dashboard/tasks/new',
      label: 'New Task',
      icon: PlusCircle,
    },
  ] as const;

  return (
    <header className="sticky top-0 z-50 border-b border-gray-200 bg-white/80 backdrop-blur-sm dark:border-gray-700 dark:bg-gray-900/80">
      <div className="mx-auto flex h-16 max-w-7xl items-center justify-between px-4">
        <Link href="/" className="text-xl font-bold text-gray-900 dark:text-white flex items-center">
          <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6 mr-2 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
          </svg>
          Todo App
        </Link>

        <button
          type="button"
          aria-label={open ? 'Close menu' : 'Open menu'}
          onClick={() => setOpen(v => !v)}
          className="inline-flex h-12 w-12 items-center justify-center rounded-xl bg-white dark:bg-gray-800 text-gray-900 dark:text-white shadow-md border border-gray-200 dark:border-gray-700 transition-all duration-200 hover:shadow-lg hover:bg-gray-50 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          {open ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
        </button>
      </div>

      {/* Drawer */}
      <div
        className={cn(
          'fixed inset-0 z-50 md:hidden',
          open ? 'pointer-events-auto' : 'pointer-events-none'
        )}
        aria-hidden={!open}
      >
        {/* Backdrop */}
        <div
          className={cn(
            'absolute inset-0 bg-black/50 transition-opacity backdrop-blur-sm',
            open ? 'opacity-100' : 'opacity-0'
          )}
          onClick={() => setOpen(false)}
        />

        {/* Panel */}
        <div
          className={cn(
            'absolute right-0 top-0 h-full w-80 max-w-[85vw] border-l border-gray-200 dark:border-gray-700 bg-gradient-to-b from-white to-gray-50 dark:from-gray-900 dark:to-gray-800 shadow-2xl transition-transform',
            open ? 'translate-x-0' : 'translate-x-full'
          )}
          role="dialog"
          aria-modal="true"
        >
          <div className="flex h-16 items-center justify-between px-4 border-b border-gray-200 dark:border-gray-700">
            <div className="min-w-0">
              <div className="text-lg font-semibold text-gray-900 dark:text-white">Menu</div>
              {auth?.user?.email ? (
                <div className="truncate text-sm text-gray-600 dark:text-gray-300 flex items-center mt-1">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-4 w-4 mr-1 text-gray-500 dark:text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
                  </svg>
                  {auth.user.email.split('@')[0]}
                </div>
              ) : (
                <div className="text-sm text-gray-600 dark:text-gray-300">Not signed in</div>
              )}
            </div>
            <button
              type="button"
              aria-label="Close menu"
              onClick={() => setOpen(false)}
              className="inline-flex h-10 w-10 items-center justify-center rounded-lg bg-gray-100 dark:bg-gray-800 text-gray-900 dark:text-white shadow-sm transition-colors hover:bg-gray-200 dark:hover:bg-gray-700 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <X className="h-5 w-5" />
            </button>
          </div>

          <nav className="px-3 py-4">
            <ul className="space-y-2">
              {navItems.map(item => {
                const Icon = item.icon;
                const active = pathname === item.href;

                return (
                  <li key={item.href}>
                    <Link
                      href={item.href}
                      className={cn(
                        'flex h-14 items-center gap-4 rounded-xl px-4 text-base font-medium transition-all duration-200',
                        active
                          ? 'bg-gradient-to-r from-blue-50 to-blue-100 text-blue-700 dark:from-blue-900/30 dark:to-blue-800/30 dark:text-blue-200 shadow-inner'
                          : 'text-gray-700 hover:bg-gray-100 dark:text-gray-200 dark:hover:bg-gray-800/50'
                      )}
                    >
                      <Icon className="h-5 w-5" />
                      <span>{item.label}</span>
                    </Link>
                  </li>
                );
              })}
            </ul>

            <div className="my-5 border-t border-gray-200 dark:border-gray-700" />

            <button
              type="button"
              onClick={() => logout.mutate()}
              className="flex h-14 w-full items-center gap-4 rounded-xl px-4 text-base font-medium text-gray-700 transition-colors hover:bg-red-50 dark:text-gray-200 dark:hover:bg-red-900/20"
            >
              <LogOut className="h-5 w-5" />
              <span>Sign out</span>
            </button>
          </nav>
        </div>
      </div>
    </header>
  );
}
