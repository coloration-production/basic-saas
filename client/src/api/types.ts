export enum BaseStatus {
  enable = 1,
  disable = 0
}

export interface RoleDto {
  id: number
  name: string
  alias: string
  status: BaseStatus
}

export interface UserDto {
  id: number
  name: string
  pwd?: string
  role: RoleDto
  role_id: number
  status: BaseStatus
  created: string
}

export interface SigninPayload {
  name: string
  pwd: string
}

export interface SigninDto {
  access_token: string
  user: UserDto
}
