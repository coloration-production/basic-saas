import {
  create,
  NConfigProvider,
  NButton,
  NForm,
  NFormItemRow,
  NInput,
  NSelect,
  NMessageProvider,
} from 'naive-ui'
import { UserModule } from '~/types'

export const install: UserModule = ({ app }) => {
  const naive = create({
    components: [
      NConfigProvider,
      NButton,
      NForm,
      NFormItemRow,
      NInput,
      NSelect,
      NMessageProvider,
    ],
  })

  app.use(naive as any)
}
