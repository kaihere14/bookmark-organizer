

import Link from "next/link"
import HeroImages from "./Landing/Hero/Hero-images"


const Hero = () => {
    return (
        <div className="mt-32 flex flex-col gap-6 relative perspective-[3000px] min-h-[900px] max-w-screen ">
            <h1 className="text-6xl font-bold max-w-4xl tracking-tight">Agents that do the work Approvals that keep you safe.</h1>
            <p className="text-neutral-400 max-w-xl text-lg tracking-wide">Deploy AI agents that plan, act through your tools, and report outcomes—without changing how your teams work.</p>
            <div className="flex gap-6 items-center">
                <Link href={"#"} className="bg-neutral-900 px-3 py-2  text-white dark:bg-neutral-200  hover:bg-neutral-700 dark:text-black dark:hover:bg-neutral-300 transition-all ease-in duration-150 rounded" >Start your free trial</Link>
                <Link href={"#"} className="hover:bg-neutral-200 dark:hover:bg-neutral-800 px-3 py-2 transition-all ease-in duration-150  rounded">View role based demos</Link>
            </div>

            <HeroImages/>
        </div>
    )
}

export default Hero
