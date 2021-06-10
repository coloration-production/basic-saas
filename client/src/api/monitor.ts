import { BaseEntityApi } from './base'
import { WindowDto, WidgetDto } from '~/types'

export const windowApi = new BaseEntityApi<WindowDto>('/window')
export const widgetApi = new BaseEntityApi<WidgetDto>('/widget')
