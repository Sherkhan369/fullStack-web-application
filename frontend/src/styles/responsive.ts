// [Task]: T039
// [From]: specs/001-fullstack-todo-auth/spec.md FR-013, SC-006
// Purpose: Centralized responsive utilities for Tailwind-based UI.

import clsx, { type ClassValue } from "clsx";
import { twMerge } from "tailwind-merge";

/**
 * Merge conditional classNames with Tailwind-aware conflict resolution.
 */
export function cn(...inputs: ClassValue[]) {
  return twMerge(clsx(inputs));
}

/**
 * Tailwind default breakpoints (px). Kept here so JS-driven responsive
 * behavior can reference the same thresholds as `sm:`, `md:`, etc.
 */
export const BREAKPOINTS = {
  sm: 640,
  md: 768,
  lg: 1024,
  xl: 1280,
  "2xl": 1536,
} as const;

export type Breakpoint = keyof typeof BREAKPOINTS;

export function mediaMin(bp: Breakpoint) {
  return `(min-width: ${BREAKPOINTS[bp]}px)`;
}

export function mediaMax(bp: Breakpoint) {
  return `(max-width: ${BREAKPOINTS[bp] - 1}px)`;
}

/**
 * Common responsive class strings.
 *
 * These are intended as small building blocks (not a full design system).
 */
export const responsive = {
  pageXPadding: "px-4 sm:px-6 lg:px-8",
  pageYPadding: "py-6 sm:py-8",
  container: "mx-auto w-full max-w-7xl",
  stackGap: "space-y-4 sm:space-y-6",
  cardPadding: "p-4 sm:p-6",
} as const;
