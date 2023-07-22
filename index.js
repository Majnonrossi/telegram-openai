require("./config")
const pkg = require('whatsapp-web.js')
const { Client, LocalAuth } = pkg
const qrcode = require('qrcode-terminal')
const fetch = require('node-fetch')

async function start() {
    const client = new Client({
        authStrategy: new LocalAuth({
            dataPath: './auth',
            userDataDir: './auth/session'
        }),
        puppeteer: {
            headless: true
        }
    })

    client.initialize()

    client.on('qr', qr => {
        qrcode.generate(qr, {small: true})
        console.log('[!] Scanner qr code')
    })

    client.on('authenticated', () => {
        console.log('[!] Authenticated')
    })

    client.on('auth_failure', m => {
        console.log(`[!] Authenticated Failure ${m}`)
    })

    client.on('disconnected', (reason) => {
        console.log('Client was logged out ' + reason)
        start()
    })

    client.on('ready', () => {
        console.log('[!] BOT Aktif')
        client.sendMessage(bot.numberId, '*[ ! ] BOT Aktif*')
    })

    client.on('message', async message => {
        console.log(message.body);

        const command = '.ai';
        if (message.body.startsWith(command)) {
            const text = message.body.slice(command.length).trim();
            if (text) {
                try {
                    const response = await fetch(`https://guru-scrapper.cyclic.app/api/chatgpt?query=${encodeURIComponent(text)}`);
                    const data = await response.json();
                    const { text: result } = data.data || {};
                    const creator = 'dark man';
                    const fullResult = `${result}\n\nCreator: ${creator}`;
                    message.reply(fullResult.trim());
                } catch (error) {
                    console.error('Error:', error); // Log the error
                    message.reply('*ERROR*');
                }
            } else {
                message.reply('يجب كتابة نص بعد الأمر.');
            }
        }
    });
}

start();
