import { BaseEntityApi } from './base'
import { UserDto } from '~/types/api'

export const userApi = new BaseEntityApi<UserDto>('/user')
