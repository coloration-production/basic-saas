import { BaseEntityApi } from './base'
import { PermissionDto, RoleDto, UserDto } from '~/types'

export const permissionApi = new BaseEntityApi<PermissionDto>('/permission')
export const roleApi = new BaseEntityApi<RoleDto>('/role')
export const userApi = new BaseEntityApi<UserDto>('/user')
