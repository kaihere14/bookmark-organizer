import React from 'react'
import Container from './components/Container'
import Hero from './components/Hero/Hero'
import SyncDevices from './components/Hero/Landing/Hero/SyncDevices'
import { Navbar } from '@/components/ui/resizable-navbar'

const page = () => {
  return (
    <div>
      <Container className='max-w-[1200px] mx-auto '>
        
        <Hero />
        <SyncDevices />
      </Container>
    </div>
  )
}

export default page
