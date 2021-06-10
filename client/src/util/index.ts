export type ComponentOption = {
  label: string,
  value: string | number | symbol
}

export function mapOptions(arr: any[], labelField = 'name', valueField = 'value'): ComponentOption[] {
  return arr.map(item => ({ ...item, label: item[labelField], value: item[valueField] }))
}

export function filterNameByOptions(options: any[] = [], nameField = 'name', valueField = 'value') {
  return function(v: string | number | symbol) {
    return (options.find(opt => opt[valueField] === v) || { [nameField]: '' })[nameField]
  }
}
