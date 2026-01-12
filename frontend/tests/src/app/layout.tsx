import type { Metadata } from 'next';
import { Inter } from 'next/font/google';
import './globals.css';
import Providers from './providers';

// [Task]: T039a, T044
// [From]: specs/001-fullstack-todo-auth/spec.md FR-013 (responsive UX) + FR-010 (JWT required), FR-015 (mobile optimization)

const inter = Inter({ subsets: ['latin'] });

export const metadata: Metadata = {
  title: 'Todo Web Application',
  description: 'A modern todo management application with authentication',
  viewport: {
    width: 'device-width',
    initialScale: 1,
    maximumScale: 1,
    userScalable: false,
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={inter.className}>
        <Providers>
          <div className="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100 dark:from-gray-900 dark:to-gray-800 font-sans antialiased">
            <div className="relative flex min-h-screen flex-col">
              <div className="flex-1">{children}</div>
            </div>
          </div>
        </Providers>
      </body>
    </html>
  );
}