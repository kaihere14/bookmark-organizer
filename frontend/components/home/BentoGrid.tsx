const BentoGrid = () => {
  return (
    <div className='mt-40 flex flex-col items-center gap-8'>
      <h1 className='text-4xl font-bold'>Features</h1>
      <div className='grid grid-cols-3 grid-rows-4 gap-3 w-full h-[600px]'>
        {/* Left — spans all 3 rows */}
        <div className='row-span-4 rounded-xl bg-amber-200'></div>

        {/* Middle top — spans 2 rows */}
        <div className='row-span-2 rounded-xl bg-red-200'></div>

        {/* Right — spans all 3 rows */}
        <div className='row-span-4 rounded-xl bg-blue-200'></div>

        {/* Middle bottom — 1 row */}
        <div className='row-span-2   rounded-xl bg-green-200'></div>
      </div>
    </div>
  )
}

export default BentoGrid
