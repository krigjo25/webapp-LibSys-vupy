import { describe, it, expect, vi } from 'vitest'
import { mount } from '@vue/test-utils'
import ActionButton from '../misc_components/ActionButton.vue'

describe('ActionButton', () => {
  it('renders properly and emits click event', async () => {
    const action = vi.fn()
    const data = {
      type: 'button',
      action: action,
      cls: 'bi bi-plus',
      name: 'Click Me'
    }
    const book = { id: 1, title: 'Test Book' }
    
    const wrapper = mount(ActionButton, {
      props: { data, book }
    })

    expect(wrapper.text()).toContain('Click Me')
    expect(wrapper.find('i').attributes('class')).toContain('bi bi-plus')
    
    await wrapper.trigger('click')
    expect(action).toHaveBeenCalledWith(book)
  })
})
