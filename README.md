# WOLproject_rb
## Description
- 이걸로 연구실 데스크탑 부팅시킬거임.
- WOL(wake on lan) 프로젝트의 라즈베리 파이 부분.
- x11 포워딩을 해도 putty ssh로 크롬 디스플레이는 확인 불가능함. 다른방법이 있겠지만, 일단은 FireFox도 써보기 위해 FireFox를 쓴다.
- 라즈베리파이는 arm7hf 아키텍쳐를 쓰므로 일반 geckodriver쓰면 안됨.
- 발열이 심한 듯 하다. 한시간에 10분은 꺼두면 좋겠는데 방법 고민중.
---

## AutoRestart
- 발열이나 시스템 안정성을 위해 30분마다 재부팅하도록 함.
> sudo crontab -e
>> */30 * * * * /sbin/reboot

- 재부팅 이후에 파이썬 스크립트가 자동 실행되도록 함.
> sudo vi /etc/xdg/lxsession/LDXE-pi/autostart
>> //맨 아랫줄에써야함.<br/>
>> lxterminal -e python /home/pi/WOLproject-rb/src/firefoxdriver.py //이건 검증됨.<br/>
>> // lxterminal -e /home/pi/WOLproject-rb/start.sh //이건 안되던데.<br/>
---
## Dependecy
- python: 2.7.16
- selenium: 3.141.0
- gecko driver: 0.23.0-arm7hf