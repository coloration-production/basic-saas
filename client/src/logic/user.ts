import { useLocalStorage } from '@vueuse/core'
import { SigninDto, STORAGE_SIGN } from '~/types'

export function useUser() {
  const u = useLocalStorage<SigninDto>(STORAGE_SIGN, {} as SigninDto)

  function setUser(user: SigninDto) {
    u.value = user
  }

  function clearUser() {
    u.value = {} as SigninDto
  }

  function noUser() {
    return Object.keys(u.value).length === 0
  }

  return { userInfo: u, setUser, clearUser, noUser }
}
