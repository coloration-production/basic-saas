
export enum BaseStatus {
  delete = 0,
  enable = 1,
  disable = 2
}

export enum WidgetType {
  frame = 1,
  camera = 2
}

export interface BaseDto {
  id: number
  status: BaseStatus
}

export interface RoleDto extends BaseDto {
  name: string
  alias: string
  permissions: number[]
}

export interface UserDto extends BaseDto {
  name: string
  pwd?: string
  role: RoleDto
  role_id: number
  created: string
}

export interface PermissionDto extends BaseDto {
  id: number
  pid: number
  name: string
  alias: string
}

export interface WidgetDto extends BaseDto {
  name: string
  url: string
  type: WidgetType
  /* eslint-disable no-use-before-define */
  windows: WindowDto[]
  info?: {
    src: ''
  }
}

export interface WindowDto extends BaseDto {
  name: string
  widgets: WidgetDto[]
  layout: string
}

export interface SigninPayload {
  name: string
  pwd: string
}

export interface SigninDto {
  access_token: string
  user: UserDto
}
