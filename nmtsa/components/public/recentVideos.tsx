import HeroVideoDialog from "@/components/ui/hero-video-dialog";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";

export function RecentVideos() {
    return (
        <main>
            <h1 className="text-3xl font-semibold">Public Videos</h1>
        <div className="flex space-x-8">
      <div className="relative w-80 py-3">
            <HeroVideoDialog
              className="dark:hidden block w-full"
              animationStyle="from-center"
              videoSrc="https://www.youtube.com/embed/qh3NGpYRG3I?si=4rb-zSdDkVK9qxxb"
              thumbnailSrc="https://startup-template-sage.vercel.app/hero-light.png"
              thumbnailAlt="Hero Video"
            />
            <p className="text-2xl text-center">Video Description</p>
      </div>
      <div className="relative w-80 py-3">
            <HeroVideoDialog
              className="dark:hidden block w-full"
              animationStyle="from-center"
              videoSrc="https://www.youtube.com/embed/qh3NGpYRG3I?si=4rb-zSdDkVK9qxxb"
              thumbnailSrc="https://startup-template-sage.vercel.app/hero-light.png"
              thumbnailAlt="Hero Video"
            />
            <p className="text-2xl text-center">Video Description</p>
      </div>
      <div className="relative w-80 py-3">
            <HeroVideoDialog
              className="dark:hidden block w-full"
              animationStyle="from-center"
              videoSrc="https://www.youtube.com/embed/qh3NGpYRG3I?si=4rb-zSdDkVK9qxxb"
              thumbnailSrc="https://startup-template-sage.vercel.app/hero-light.png"
              thumbnailAlt="Hero Video"
            />
            <p className="text-2xl text-center">Video Description</p>
      </div>
      <div className="relative w-80 py-3">
            <HeroVideoDialog
              className="dark:hidden block w-full"
              animationStyle="from-center"
              videoSrc="https://www.youtube.com/embed/qh3NGpYRG3I?si=4rb-zSdDkVK9qxxb"
              thumbnailSrc="https://startup-template-sage.vercel.app/hero-light.png"
              thumbnailAlt="Hero Video"
            />
            <p className="text-2xl text-center">Video Description</p>
      </div>
      </div>
      </main>
    );
  }