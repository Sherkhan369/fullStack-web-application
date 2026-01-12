import Link from 'next/link';

export default function AuthPage() {
  return (
    <div className="text-center">
      <h1 className="text-2xl font-bold mb-6">Welcome</h1>
      <p className="text-gray-600 dark:text-gray-300 mb-8">
        Please choose an option to get started
      </p>

      <div className="space-y-4">
        <Link
          href="/login"
          className="block w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 px-4 rounded-lg transition-colors duration-200"
        >
          Sign In
        </Link>

        <Link
          href="/signup"
          className="block w-full border border-gray-300 dark:border-gray-600 hover:bg-gray-50 dark:hover:bg-gray-700 text-gray-700 dark:text-gray-200 font-semibold py-3 px-4 rounded-lg transition-colors duration-200"
        >
          Create Account
        </Link>

        <Link
          href="/"
          className="block text-sm text-blue-600 hover:text-blue-500"
        >
          ← Back to Home
        </Link>
      </div>
    </div>
  );
}