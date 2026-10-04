
(() => {
  const navToggle = document.querySelector('.nav-toggle');
  const nav = document.querySelector('.main-nav');
  navToggle?.addEventListener('click', () => nav?.classList.toggle('open'));

  // 12 minute practice timer
  const display = document.getElementById('timeDisplay');
  if (display) {
    const total = 12*60;
    const stages = [
      {until:90,title:'坐下来，让自己到达这里。',prompt:'注意身体、房间和此刻的状态。不需要马上安静。',label:'到场'},
      {until:180,title:'允许声音与念头存在。',prompt:'不跟随，也不排斥。你只是在这里。',label:'安顿'},
      {until:600,title:'从“我要做什么”转向等待。',prompt:'不必寻找什么。只是等待，并留意什么正在出现。',label:'等候'},
      {until:690,title:'留意有没有什么变得稍微清楚。',prompt:'不是逼出答案。只是注意重量、方向、反复出现的东西。',label:'辨识'},
      {until:720,title:'准备结束。',prompt:'把注意带回身体和房间。带走问题，不必带走结论。',label:'返回'}
    ];
    let remain=total, timer=null, running=false;
    const progress=document.getElementById('timerProgress');
    const stageTitle=document.getElementById('stageTitle');
    const stagePrompt=document.getElementById('stagePrompt');
    const stageIndex=document.getElementById('stageIndex');
    const track=document.getElementById('stageTrack');
    track.innerHTML=stages.map(()=>'<span></span>').join('');
    const fmt=n=>`${String(Math.floor(n/60)).padStart(2,'0')}:${String(n%60).padStart(2,'0')}`;
    function bell(){ try{ const ctx=new (window.AudioContext||window.webkitAudioContext)(); const o=ctx.createOscillator(),g=ctx.createGain(); o.type='sine';o.frequency.value=523.25;g.gain.setValueAtTime(0.0001,ctx.currentTime);g.gain.exponentialRampToValueAtTime(.08,ctx.currentTime+.03);g.gain.exponentialRampToValueAtTime(.0001,ctx.currentTime+1.4);o.connect(g).connect(ctx.destination);o.start();o.stop(ctx.currentTime+1.5);}catch(e){} }
    function render(){
      display.textContent=fmt(remain);
      const elapsed=total-remain; const stage=stages.findIndex(s=>elapsed < s.until); const idx=stage<0?stages.length-1:stage;
      stageTitle.textContent=stages[idx].title; stagePrompt.textContent=stages[idx].prompt; stageIndex.textContent=stages[idx].label;
      [...track.children].forEach((el,i)=>el.classList.toggle('active',i<=idx));
      const circumference=327; progress.style.strokeDashoffset=(circumference*(1-remain/total)).toFixed(1);
    }
    function tick(){ if(remain<=0){clearInterval(timer);running=false;bell();return;} remain--; render(); }
    document.getElementById('startTimer').onclick=()=>{ if(running)return; running=true; bell(); timer=setInterval(tick,1000); };
    document.getElementById('pauseTimer').onclick=()=>{clearInterval(timer);running=false;};
    document.getElementById('resetTimer').onclick=()=>{clearInterval(timer);running=false;remain=total;render();};
    render();
    const ids=['r1','r2','r3']; ids.forEach(id=>{const el=document.getElementById(id); el.value=localStorage.getItem('meeting_'+id)||'';});
    document.getElementById('saveReflection').onclick=()=>{ids.forEach(id=>localStorage.setItem('meeting_'+id,document.getElementById(id).value));document.getElementById('saveStatus').textContent='已保存在此浏览器';};
    document.getElementById('clearReflection').onclick=()=>{ids.forEach(id=>{localStorage.removeItem('meeting_'+id);document.getElementById(id).value='';});document.getElementById('saveStatus').textContent='已清空';};
  }

  // Ministry self-test
  const mt=document.getElementById('ministryTest');
  if(mt){document.getElementById('evaluateMinistry').onclick=()=>{const n=mt.querySelectorAll('input:checked').length; const out=document.getElementById('ministryResult'); out.textContent=n>=4?'你已经在做一件很重要的事：让“说话的冲动”先接受等待。即使如此，也可以再多等一会儿。':n>=2?'可能值得继续等待。先别急着把“我很想说”解释成“我应该说”。':'先继续沉默也许更忠实。没有说出来，并不等于没有参与。';};}

  // Business case lab
  const caseLab=document.getElementById('caseLab');
  if(caseLab){const res=document.getElementById('caseResult');caseLab.querySelectorAll('[data-case]').forEach(b=>b.onclick=()=>{const k=b.dataset.case;res.innerHTML={vote:'<b>多数表决</b>优化的是速度与程序明确。7:3 很快有结果，但“离开原社区意味着什么”可能仍未被共同体真正消化。',consensus:'<b>共识（Consensus）</b>优化的是可接受度。大家会继续协商方案，但也可能把目标缩成“每个人都勉强能接受”。',sense:'<b>聚会的共同辨识（Sense of the Meeting）</b>会把问题从“新址好不好”下沉到“我们的使命、邻里关系与可持续性中，什么方向最忠实？”结果可能是搬、也可能是不搬，甚至是暂缓决定。'}[k];});}

  // Clearness question lab
  const qLab=document.getElementById('questionLab');
  if(qLab){const data=[
    ['“你有没有想过，其实你应该先休息一段时间？”','advice','问题里已经塞进了答案：先休息。可以改问：“当你想象继续撑下去和停下来时，分别注意到什么？”'],
    ['“在这个决定里，哪一种担心最容易盖过你自己的声音？”','open','这是开放问题。它没有替对方命名答案，而是邀请他辨认内部声音。'],
    ['“你是不是因为太在意父母，所以才不敢离开？”','advice','这是一种解释加判断。可以改问：“在你考虑离开时，哪些人的声音会出现？它们分别对你有什么影响？”'],
    ['“如果暂时不用向任何人证明什么，你会怎样描述自己真正想保护的东西？”','open','这是开放问题。它提供一个角度，但不规定内容。']
  ];let i=0;const ex=document.getElementById('questionExample'),fb=document.getElementById('questionFeedback');function show(){ex.textContent=data[i][0];fb.textContent='先判断，再看为什么。';}qLab.querySelectorAll('[data-q]').forEach(b=>b.onclick=()=>{fb.textContent=(b.dataset.q===data[i][1]?'✓ ':'再看看：')+data[i][2];});document.getElementById('nextQuestion').onclick=()=>{i=(i+1)%data.length;show();};show();}

  // Glossary search & filter
  const gSearch=document.getElementById('glossarySearch');
  if(gSearch){let active='all';const cards=[...document.querySelectorAll('.glossary-card')];function apply(){const q=gSearch.value.trim().toLowerCase();cards.forEach(c=>{const txt=c.dataset.term+' '+c.textContent.toLowerCase();const cat=c.querySelector('span').textContent; c.style.display=(!q||txt.includes(q))&&(active==='all'||cat===active)?'block':'none';});}gSearch.oninput=apply;document.querySelectorAll('.filter').forEach(b=>b.onclick=()=>{document.querySelectorAll('.filter').forEach(x=>x.classList.remove('active'));b.classList.add('active');active=b.dataset.filter;apply();});}
})();
