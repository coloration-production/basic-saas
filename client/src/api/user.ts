import { base } from './base'
import { UserDto } from '~/types/api'

function users(filter?: Partial<UserDto>) {
  return base.get<UserDto[]>('/users', filter)
}

export const userApi = {
  users,
}
