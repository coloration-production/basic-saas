import { base } from './base'
import { RoleDto } from '~/types'

function roles(filter?: Partial<RoleDto>) {
  return base.get<RoleDto[]>('/roles', filter)
}

function getRole(id: number) {
  return base.get<RoleDto>('/role', { id })
}

function createRole(role: Partial<RoleDto>) {
  return base.post<RoleDto>('/role', role)
}

function modifyRole(id: number, role: Partial<RoleDto>) {
  return base.patch<RoleDto>(`/role/${id}`, role)
}

export const roleApi = {
  roles,
  getRole,
  createRole,
  modifyRole,
}
