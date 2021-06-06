import { base } from './base'
import { SigninDto, SigninPayload } from './types'

function signin(payload: SigninPayload) {
  return base.post('/signin', payload)
    .then((res: SigninDto) => {
      const { access_token } = res

      base.conf.headers = Object.assign(base.conf.headers, {
        Authorization: `JWT ${access_token}`,
      })
      return res.user
    })
}

export const accessApi = {
  signin,
}
