import HeroVideoDialog from "@/components/ui/hero-video-dialog";
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card";
import Image from "next/image";
export function RecentArticles() {
    return (
        <main>
            <h1 className="text-3xl font-semibold">Public Articles</h1>
        <div className="flex space-x-8">
        <Card
                  className="overflow-hidden w-80" x-chunk="dashboard-07-chunk-4"
                >
                  <CardHeader>
                    <CardTitle className="text-lg">Product Images</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="grid gap-2">
                      <Image
                        alt="Product image"
                        className="aspect-square w-full rounded-md object-cover"
                        height="150"
                        src="/placeholder.svg"
                        width="80"
                      />
                    </div>
                  </CardContent>
                </Card>
                <Card
                  className="overflow-hidden w-80" x-chunk="dashboard-07-chunk-4"
                >
                  <CardHeader>
                    <CardTitle className="text-lg">Product Images</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="grid gap-2">
                      <Image
                        alt="Product image"
                        className="aspect-square w-full rounded-md object-cover"
                        height="150"
                        src="/placeholder.svg"
                        width="80"
                      />
                    </div>
                  </CardContent>
                </Card>
                <Card
                  className="overflow-hidden w-80" x-chunk="dashboard-07-chunk-4"
                >
                  <CardHeader>
                    <CardTitle className="text-lg">Product Images</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="grid gap-2">
                      <Image
                        alt="Product image"
                        className="aspect-square w-full rounded-md object-cover"
                        height="150"
                        src="/placeholder.svg"
                        width="80"
                      />
                    </div>
                  </CardContent>
                </Card>
                <Card
                  className="overflow-hidden w-80" x-chunk="dashboard-07-chunk-4"
                >
                  <CardHeader>
                    <CardTitle className="text-lg">Product Images</CardTitle>
                  </CardHeader>
                  <CardContent>
                    <div className="grid gap-2">
                      <Image
                        alt="Product image"
                        className="aspect-square w-full rounded-md object-cover"
                        height="150"
                        src="/placeholder.svg"
                        width="80"
                      />
                    </div>
                  </CardContent>
                </Card>
      </div>
      </main>
    );
  }