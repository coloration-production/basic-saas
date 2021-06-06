import { Asker } from '@coloration/asker'
import { } from 'vue-router'
import { SigninDto, STORAGE_SIGN } from '../types'

export const base = new Asker({
  baseUrl: 'http://localhost:5678',
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
    if (res.status === 401) {
      localStorage.setItem('@@user', '{}')
      return
    }

    return res.data
  },
})
