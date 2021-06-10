import { GlobalThemeOverrides } from 'naive-ui'

export function useNaiveThemeOverrides() {
  const themeOverrides: GlobalThemeOverrides = {
    common: {
      primaryColor: '#6366f1',
      primaryColorHover: '#4f46e5',
      primaryColorPressed: '#4f46e5',
      primaryColorSuppl: '#4f46e5',
      borderRadius: '2px',
      borderRadiusSmall: '2px',
    },
    // Button: {
    //   textColor: '#FF0000',
    // },
    // Select: {
    //   peers: {
    //     InternalSelection: {
    //       textColor: '#FF0000',
    //     },
    //   },
    // },
  }

  return {
    themeOverrides,
  }
}
