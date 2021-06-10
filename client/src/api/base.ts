import { Asker, HttpStatus } from '@coloration/asker'
import { } from 'vue-router'
import { SigninDto, STORAGE_SIGN } from '~/types'

export const base = new Asker({
  baseUrl: 'http://localhost:5678',
  errorResponseType: 'json',
  before: (conf) => {
    if (conf.url === '/signin') return conf

    if (!conf.headers || !conf.headers.Authorization) {
      const userInfo: SigninDto = JSON.parse(localStorage.getItem(STORAGE_SIGN) || '{}')
      if (!userInfo.access_token) throw new Error('401')
      conf.headers = Object.assign(base.conf.headers, {
        Authorization: `JWT ${userInfo.access_token}`,
      })
    }

    return conf
  },
  after: (res) => {
    return res.data
  },
  catcher: (e) => {
    if (e.status === HttpStatus.unauthorized) {
      localStorage.setItem(STORAGE_SIGN, '{}')
      const { protocol, host } = window.location
      window.location.href = `${protocol}//${host}/access/signin`
    }
  },
})

export class BaseEntityApi<T> {
  path: string

  constructor(path: string) {
    this.path = path
  }

  list(filter?: Partial<T>) {
    return base.get<T[]>(`${this.path}s`, filter)
  }

  get(id: number) {
    return base.get<T>(this.path, { id })
  }

  create(role: Partial<T>) {
    return base.post<T>(this.path, role)
  }

  modify(id: number, role: Partial<T>) {
    return base.patch<T>(`${this.path}/${id}`, role)
  }

  delete(id: number) {
    return base.delete(`${this.path}/${id}`)
  }
}
