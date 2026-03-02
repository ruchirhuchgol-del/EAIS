import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";
import { Toaster } from "@/components/ui/toaster";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "EAIS Platform | Enterprise Architecture Intelligence System",
  description: "AI-Powered Enterprise Architecture Intelligence System - Transform product requirements into production-ready, enterprise-grade system architectures. Features multi-agent AI orchestration, compliance automation, and business impact analysis.",
  keywords: ["Enterprise Architecture", "AI", "Multi-Agent Systems", "Compliance", "GDPR", "SOC2", "Cloud Architecture", "TCO Analysis", "ROI"],
  authors: [{ name: "EAIS Team" }],
  icons: {
    icon: "/favicon.ico",
  },
  openGraph: {
    title: "EAIS Platform",
    description: "AI-Powered Enterprise Architecture Intelligence System",
    siteName: "EAIS Platform",
    type: "website",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased bg-background text-foreground`}
      >
        {children}
        <Toaster />
      </body>
    </html>
  );
}
