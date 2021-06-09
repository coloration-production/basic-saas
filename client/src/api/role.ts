import { BaseEntityApi } from './base'
import { RoleDto } from '~/types'

export const roleApi = new BaseEntityApi<RoleDto>('/role')
