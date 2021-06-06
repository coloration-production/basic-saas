import { base } from './base'
import { SigninPayload } from '~/types'

function signin(payload: SigninPayload) {
  return base.post('/signin', payload)
}

function signout() {
  return base.patch('/signout', null, { responseType: 'text' })
}

export const accessApi = {
  signin, signout,
}
