import { base } from './base'
import { UserDto } from '~/types/api'

function users(filter?: Partial<UserDto>) {
  return base.get<UserDto[]>('/users', filter)
}

function getUser(id: number) {
  return base.get<UserDto>('/user', { id })
}

function createUser(user: Partial<UserDto>) {
  return base.post<UserDto>('/user', user)
}

function modifyUser(id: number, user: Partial<UserDto>) {
  return base.patch<UserDto>(`/user/${id}`, user)
}

export const userApi = {
  users, getUser, createUser, modifyUser,
}
