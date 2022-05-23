# 使用mpeg裁剪视频里的字幕部分
for file in `ls raw`
do

	if [ -f "raw/$file" ]
	then
		echo $file
		ffmpeg -i "raw/$file" -filter:v "crop=352:34:0:254" "crop/${file}_crop.mp4"
	else
		echo "$file not file"
	fi
done
