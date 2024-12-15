use std::env;
use std::io::{stdin,copy};
use std::iter::repeat;
use std::process::exit;
use std::process::Command;
use std::ptr::null_mut as NULL;
use base64::{engine::general_purpose::STANDARD, read::DecoderReader};

use crypto::rc4::Rc4;

use crypto::symmetriccipher::SynchronousStreamCipher;
use winapi::um::winuser;

fn get_env(variable: &str) -> String {
    match env::var(variable) {
        Ok(val) => val,
        Err(_e) => "".to_string()
    }
}

fn main() {
    let env_var = get_env("crispy_cookie");
    if env_var != "" {

        // Decode base64 String
        let mut env_var_b = env_var.as_bytes();
        let mut b64decoded: Vec<u8> = vec![];
        let mut decoder = DecoderReader::new(&mut env_var_b, &STANDARD);
        let _ = copy(&mut decoder, &mut b64decoded);

        if b64decoded[0 .. 4] == [0x13,0x37,0x13,0x37] {
            let user_inp = get_env("user_flag");
            if user_inp.as_bytes().len() != b64decoded.len() - 4 {
                let l_msg: Vec<u16> = "Nope\0".encode_utf16().collect();
                let l_title: Vec<u16> = "Wrong Flag\0".encode_utf16().collect();
                unsafe {
                    winuser::MessageBoxW(NULL(), l_msg.as_ptr(), l_title.as_ptr(), winuser::MB_OK | winuser::MB_ICONERROR);
                }
                exit(1);
            }
            let mut i: usize = 0;
            while i < user_inp.len() {
                if user_inp.as_bytes()[i] != b64decoded[i+4] {
                    let l_msg: Vec<u16> = "Nope\0".encode_utf16().collect();
                    let l_title: Vec<u16> = "Wrong Flag\0".encode_utf16().collect();
                    unsafe {
                        winuser::MessageBoxW(NULL(), l_msg.as_ptr(), l_title.as_ptr(), winuser::MB_OK | winuser::MB_ICONERROR);
                    }
                    exit(1);
                }
                i += 1;
            }
            let l_msg: Vec<u16> = "Correct!!!\0".encode_utf16().collect();
                let l_title: Vec<u16> = "OMG YOU DID IT\0".encode_utf16().collect();
                unsafe {
                    winuser::MessageBoxW(NULL(), l_msg.as_ptr(), l_title.as_ptr(), winuser::MB_OK | winuser::MB_ICONEXCLAMATION);
                }
            exit(0);
        }

        let key_len: usize = b64decoded[0].into();
        let junk_len: usize = b64decoded[1].into();
        let key: &[u8] = (&b64decoded[2+junk_len .. 2+junk_len+key_len]).into();

        let mut enc_data: &[u8] = &b64decoded[2+junk_len+key_len .. b64decoded.len()];

        let mut rc4 = Rc4::new(key);
        let mut result: Vec<u8> = repeat(0).take(enc_data.len()).collect();
        rc4.process(&mut enc_data, &mut result);

        env::set_var("crispy_cookie",base64::encode(result.clone()))        

    }
    else {
        env::set_var("crispy_cookie","DBziwCh2U7mVnRoEzhXJXdyFwQYf0rwZI0oj76TokRPp4/mIJpd/tA8xJZ4nXeUlYl9NY0XI+d55ApbCKhWjLsKfPJepW7vCe0fJF2gG2J1nJJxxgCFpr4+kq1kE7pCXBvVcGf4nWv2nLcqDKN+g7IS4d1owd2qq61GPyHefQDi3lVn8H/FzO0COp+9BPsJc8GVsWCJZ2AeYhFf91vXP+wyFj6RPmylH8yz37bzE/3bYV6OK3t/u2YbQj/JWlsGQk5kjuELogZYNUn9c2oSfsaTqMQmKUXTRJMFp0NVubAEJtQPg7AzvTY5oX0BABBTKMpLIJsXhhs036ZYue3oBaOqPq/Cen0ek89FeGxLt98nEFKk4xvq9+XtI1ZSYqfYw7lCtl49yNjuTfa7fE51netthfoASWSImpV3vw3WqNBCO/ifcrq3SIarEJIulw52TfqS5+SXPgLAzXDaWz6E/41gp1GyegON4/mtzP64qr55zNypCW5KQmYlXN+aTDNmD2uKRAKENSh6F5Kfixz9TDPjzKvjJ66zSjcN7uYVnytQHxIAc6WCA/q51oYkLpwZK5tSIkAFyXbM6xpCNdnHsMEVv8RhuuooOz/4luibS5Caw7NK9bR6aCwCNrDv45hHpE/XWHOdEsm5a5hmfaZr3vhgql82MsKHbUsE3nck0YAimrvXOdDxumXGc9O8gBOCV9Qo3+3KyBYyp4vjgtKPfJaxhFCVigAkshIEKfGgQLAgfg0jB7rmjYFZaCo+NMpf3WcjCSG/bGiPekUFxkV0ICppM+Llu1k/We1JmaanobOaJIe+YKTvG6duNRqwm3wDnEA==");
        // Print text to the console.
        println!("Hey there. Umm... i only have a simple request for you");
        println!("Enter the flag: ");
        let mut user_inp = String::new();
        stdin().read_line(&mut user_inp).expect("Umm are you sure about that?");
        if let Some('\n')=user_inp.chars().next_back() {
            user_inp.pop();
        }
        if let Some('\r')=user_inp.chars().next_back() {
            user_inp.pop();
        }
        env::set_var("user_flag",user_inp);
    }
    let path;
    match env::current_exe() {
        Ok(exe_path) => path = exe_path,
        Err(_e) => exit(1),
    };    
    let _ = Command::new(path)
        .spawn();
}