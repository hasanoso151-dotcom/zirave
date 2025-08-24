import { serve } from "https://deno.land/std@0.168.0/http/server.ts"

const corsHeaders = {
  'Access-Control-Allow-Origin': '*',
  'Access-Control-Allow-Headers': 'authorization, x-client-info, apikey, content-type',
}

interface ModerationRequest {
  content: string;
  type?: 'message' | 'product' | 'profile';
}

interface ModerationResponse {
  isAppropriate: boolean;
  confidence: number;
  flaggedWords: string[];
  suggestion?: string;
}

serve(async (req) => {
  // Handle CORS preflight requests
  if (req.method === 'OPTIONS') {
    return new Response('ok', { headers: corsHeaders })
  }

  try {
    const { content, type = 'message' }: ModerationRequest = await req.json()

    // Simple content moderation rules for Turkish agricultural platform
    const inappropriateWords = [
      'spam', 'scam', 'fake', 'sahte', 'dolandırıcı', 'hileli',
      'kötü', 'berbat', 'rezalet', 'çöp', 'boktan'
    ]

    const suspiciousPatterns = [
      /\b\d{4}\s?\d{4}\s?\d{4}\s?\d{4}\b/, // Credit card patterns
      /\b\d{11}\b/, // Phone number patterns
      /bitcoin|kripto|yatırım|garanti/i, // Investment scams
    ]

    const flaggedWords: string[] = []
    const lowerContent = content.toLowerCase()

    // Check for inappropriate words
    inappropriateWords.forEach(word => {
      if (lowerContent.includes(word)) {
        flaggedWords.push(word)
      }
    })

    // Check for suspicious patterns
    const hasSuspiciousPattern = suspiciousPatterns.some(pattern => 
      pattern.test(content)
    )

    const isAppropriate = flaggedWords.length === 0 && !hasSuspiciousPattern
    const confidence = isAppropriate ? 0.95 : 0.85

    let suggestion: string | undefined
    if (!isAppropriate) {
      if (type === 'message') {
        suggestion = 'Mesajınızda uygunsuz içerik tespit edildi. Lütfen nezaket kurallarına uygun bir şekilde yazın.'
      } else if (type === 'product') {
        suggestion = 'Ürün açıklamanızda uygunsuz ifadeler bulunuyor. Lütfen düzenleyin.'
      }
    }

    const response: ModerationResponse = {
      isAppropriate,
      confidence,
      flaggedWords,
      suggestion
    }

    return new Response(
      JSON.stringify(response),
      {
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        status: 200,
      },
    )
  } catch (error) {
    return new Response(
      JSON.stringify({ error: error.message }),
      {
        headers: { ...corsHeaders, 'Content-Type': 'application/json' },
        status: 400,
      },
    )
  }
})