import Container from "@/components/layout/Container"
import Hero from "@/components/home/Hero"
import SyncDevices from "@/components/home/SyncDevices"
import BentoGrid from "@/components/home/BentoGrid"

const page = () => {
  return (
    <div>
      <Container className='max-w-[1200px] mx-auto'>
        <Hero />
        <SyncDevices />
        <BentoGrid />
      </Container>
    </div>
  )
}

export default page
