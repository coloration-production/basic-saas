import { BaseEntityApi } from './base'
import { PermissionDto } from '~/types'

export const permissionApi = new BaseEntityApi<PermissionDto>('/permission')
