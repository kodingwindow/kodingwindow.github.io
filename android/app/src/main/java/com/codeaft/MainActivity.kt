package com.godarda

import android.annotation.SuppressLint
import android.app.UiModeManager
import android.content.Context
import android.content.Intent
import android.net.ConnectivityManager
import android.net.Uri
import android.os.Bundle
import android.view.View
import android.view.WindowManager
import android.webkit.WebResourceRequest
import android.webkit.WebSettings
import android.webkit.WebView
import android.webkit.WebViewClient
import android.widget.Button
import android.widget.Toast
import androidx.activity.OnBackPressedCallback
import androidx.appcompat.app.AppCompatActivity
import androidx.core.net.toUri


class MainActivity : AppCompatActivity() {
    lateinit var webview: WebView

    @SuppressLint("SetJavaScriptEnabled")
    override fun onCreate(savedInstanceState: Bundle?) {
        val uiModeManager = getSystemService(Context.UI_MODE_SERVICE) as UiModeManager
        val currentMode = uiModeManager.nightMode
        if (currentMode == UiModeManager.MODE_NIGHT_YES) {
            setTheme(R.style.AppTheme_Dark)
        } else {
            setTheme(R.style.AppTheme_Light)
        }
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        webview = findViewById(R.id.webView)
        webview.settings.safeBrowsingEnabled = true
        webview.settings.domStorageEnabled = true
        webview.settings.useWideViewPort = false
        webview.settings.displayZoomControls = false
        webview.settings.builtInZoomControls = false
        webview.settings.allowFileAccess = false
        webview.settings.allowContentAccess = false
        webview.settings.setSupportZoom(false)
        webview.settings.textZoom = 100
        webview.settings.cacheMode = WebSettings.LOAD_DEFAULT
        webview.settings.javaScriptEnabled = true
        webview.settings.loadsImagesAutomatically = true
        webview.settings.userAgentString += "GoDarda"
        webview.webViewClient = WebViewClient()
        webview.isVerticalScrollBarEnabled = false
        webview.isHorizontalScrollBarEnabled = false
        webview.overScrollMode = View.OVER_SCROLL_NEVER
        webview.isHapticFeedbackEnabled = false
        window.setSoftInputMode(WindowManager.LayoutParams.SOFT_INPUT_ADJUST_NOTHING)
        if ((this@MainActivity.getSystemService(CONNECTIVITY_SERVICE) as ConnectivityManager).activeNetwork == null) {
            setContentView(R.layout.alert_dialog)
            val btn = findViewById<Button>(R.id.tryagain)
            btn.setOnClickListener { recreate() }
        } else {
            webview.loadUrl("https://godarda.github.io")
        }
        webview.webViewClient = object : WebViewClient() {
            override fun shouldOverrideUrlLoading(
                view: WebView,
                request: WebResourceRequest
            ): Boolean {
                if ((this@MainActivity.getSystemService(CONNECTIVITY_SERVICE) as ConnectivityManager).activeNetwork == null) {
                    setContentView(R.layout.alert_dialog)
                    val btn = findViewById<Button>(R.id.tryagain)
                    btn.setOnClickListener { recreate() }
                }
                var url = request.url.toString()
                if (url.startsWith("https://godarda.github.io")) {
                    return "$url/" == webview.getUrl()
                }
                if (url.startsWith("share")) {
                    url = url.replace("share:", "").replace(".html", "")
                    val shareIntent = Intent(Intent.ACTION_SEND)
                    shareIntent.setType("text/plain")
                    shareIntent.putExtra(Intent.EXTRA_TITLE, view.title.toString())
                    shareIntent.putExtra(Intent.EXTRA_TEXT, url)
                    startActivity(Intent.createChooser(shareIntent, title))
                    return true
                }
                if (url.startsWith("clear:")) {
                    webview.clearHistory()
                    webview.clearCache(true)
                    webview.clearFormData()
                    return true
                }
                if (url.startsWith("https://giscus.app/") ||
                    (url.startsWith("https://github.com/login") ||
                            (url.startsWith("https://github.com/session")))
                ) {
                    webview.loadUrl(url)
                    return true
                }
                if (!url.startsWith("https://godarda.github.io")) {
                    startActivity(Intent(Intent.ACTION_VIEW, url.toUri()))
                    return true
                }
                return true
            }
        }
        onBackPressedDispatcher.addCallback(this, object : OnBackPressedCallback(true) {
            override fun handleOnBackPressed() {
                if (webview.title.toString() == "GoDarda")
                    finishAffinity()
                else if (webview.url.toString()
                        .startsWith("https://github.com/sessions/two-factor")
                ) {
                    Toast.makeText(
                        webview.context,
                        "Session Expired",
                        Toast.LENGTH_SHORT
                    ).show()
                    finishAffinity()
                } else if (webview.canGoBack())
                    webview.goBack()
                else
                    finishAffinity()
            }
        })
    }
}