import { Navbar } from "@/components/Navbar";
import GradualSpacing from "@/components/ui/gradual-spacing";
import SparklesText from "@/components/ui/sparkles-text";
import { RecentVideos } from "@/components/public/recentVideos";
import { RecentArticles } from "@/components/public/recentArticles";
import { Hero } from "@/components/public/hero";
import { Testimonials } from "@/components/public/testimonials";

export default function Page() {
    return (
        <div className="container mx-auto py-10">
        <Navbar />
        <GradualSpacing
      className="font-display text-center text-4xl font-bold -tracking-widest  text-primary md:text-7xl md:leading-[5rem]"
      text="Librarian"
    />
    <Hero />
    <section>
        <RecentVideos />
        <br></br>
        <RecentArticles />
    </section>
    <Testimonials />
      </div>
    )
}