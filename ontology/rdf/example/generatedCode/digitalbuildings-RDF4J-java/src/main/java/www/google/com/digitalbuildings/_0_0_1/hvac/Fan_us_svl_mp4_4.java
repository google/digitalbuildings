package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IDischarge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Discharge_air_temperature_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.IExhaust_air_static_pressure_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Exhaust_air_static_pressure_sensor;

/**
* Class Fan_us_svl_mp4_4 
* Hash:b0ca60c549d1ba9493310cb1e832003a645a704cb4e659e28312336fc8048222; Entities: US-SVL-MP4:FAN:KEF-1 SF
*/
@SuppressWarnings("serial")
public class Fan_us_svl_mp4_4 extends www.google.com.digitalbuildings._0_0_1.hvac.Fan_ss_vsc implements IFan_us_svl_mp4_4{

	IRI newInstance;
	public Fan_us_svl_mp4_4(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_us_svl_mp4_4"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesExhaust_air_static_pressure_sensor (IExhaust_air_static_pressure_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IExhaust_air_static_pressure_sensor> getUsesExhaust_air_static_pressure_sensor (){
		Set<IExhaust_air_static_pressure_sensor> UsesExhaust_air_static_pressure_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Exhaust_air_static_pressure_sensor) {
				UsesExhaust_air_static_pressure_sensor.add((Exhaust_air_static_pressure_sensor)action);
			}
		});
		return UsesExhaust_air_static_pressure_sensor;
	}

	public static Set<IFan_us_svl_mp4_4> getAllFan_us_svl_mp4_4sObjectsCreated(){
		Set<IFan_us_svl_mp4_4> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_us_svl_mp4_4")).subjects().stream()
		.map(mapper->(IFan_us_svl_mp4_4)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}