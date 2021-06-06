import { base } from './base'
import { RoleDto } from '~/types/api'

function roles(filter?: Partial<RoleDto>) {
  return base.get<RoleDto[]>('/roles', filter)
}

export const roleApi = {
  roles,
}
