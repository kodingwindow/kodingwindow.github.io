package com.godarda

import android.annotation.SuppressLint
import android.app.UiModeManager
import android.content.Context
import android.content.Intent
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity

@SuppressLint("CustomSplashScreen")
class SplashActivity : AppCompatActivity() {
    lateinit var version: TextView

    @SuppressLint("SetTextI18n")
    override fun onCreate(savedInstanceState: Bundle?) {
        val uiModeManager = getSystemService(Context.UI_MODE_SERVICE) as UiModeManager
        val currentMode = uiModeManager.nightMode
        if (currentMode == UiModeManager.MODE_NIGHT_YES) {
            setTheme(R.style.AppTheme_Splash);
        } else {
            setTheme(R.style.AppTheme_Splash);
        }
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)
        version = findViewById(R.id.appversion)
        version.text = "App Version " + packageManager.getPackageInfo(packageName, 0).versionName
        Handler(Looper.getMainLooper()).postDelayed({
            val i = Intent(this@SplashActivity, MainActivity::class.java)
            startActivity(i)
            finish()
        }, 2000)
    }
}