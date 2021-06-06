import { ViteSSGContext } from 'vite-ssg'

export * from './views'
export * from './api'

export const STORAGE_SIGN = '@@application'
export type UserModule = (ctx: ViteSSGContext) => void
