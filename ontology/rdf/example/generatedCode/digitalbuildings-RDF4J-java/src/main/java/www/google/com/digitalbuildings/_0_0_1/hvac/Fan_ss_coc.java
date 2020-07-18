package www.google.com.digitalbuildings._0_0_1.hvac;

import digitalbuildings.global.util.GLOBAL;

import org.eclipse.rdf4j.model.IRI;
import org.eclipse.rdf4j.model.vocabulary.RDF;
import java.util.HashSet;
import java.util.Set;
import java.util.stream.Collectors;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co_concentration_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_co_concentration_setpoint;
import www.google.com.digitalbuildings._0_0_1.fields.IZone_air_co_concentration_sensor;
import www.google.com.digitalbuildings._0_0_1.fields.Zone_air_co_concentration_sensor;

/**
* Class Fan_ss_coc 
* On/off fan with carbon monoxide control.
*/
@SuppressWarnings("serial")
public class Fan_ss_coc extends www.google.com.digitalbuildings._0_0_1.hvac.Ss implements IFan_ss_coc{

	IRI newInstance;
	public Fan_ss_coc(String namespace, String instanceId) {
		super(namespace, instanceId);

		newInstance = GLOBAL.factory.createIRI(namespace, instanceId);
		GLOBAL.model.add(this, RDF.TYPE, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_ss_coc"));
	}

	public IRI iri()
	{
		return newInstance;
	}


  public void addUsesZone_air_co_concentration_sensor (IZone_air_co_concentration_sensor parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_co_concentration_sensor> getUsesZone_air_co_concentration_sensor (){
		Set<IZone_air_co_concentration_sensor> UsesZone_air_co_concentration_sensor = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_co_concentration_sensor) {
				UsesZone_air_co_concentration_sensor.add((Zone_air_co_concentration_sensor)action);
			}
		});
		return UsesZone_air_co_concentration_sensor;
	}


  public void addUsesZone_air_co_concentration_setpoint (IZone_air_co_concentration_setpoint parameter)
	{
		GLOBAL.model.add(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), parameter);
	}

	public Set<IZone_air_co_concentration_setpoint> getUsesZone_air_co_concentration_setpoint (){
		Set<IZone_air_co_concentration_setpoint> UsesZone_air_co_concentration_setpoint = new HashSet<>();
		GLOBAL.model.filter(this, GLOBAL.factory.createIRI("http://www.google.com/digitalbuildings/0.0.1#uses"), null)
		.objects().forEach(action->{
			if(action instanceof Zone_air_co_concentration_setpoint) {
				UsesZone_air_co_concentration_setpoint.add((Zone_air_co_concentration_setpoint)action);
			}
		});
		return UsesZone_air_co_concentration_setpoint;
	}

	public static Set<IFan_ss_coc> getAllFan_ss_cocsObjectsCreated(){
		Set<IFan_ss_coc> objects = new HashSet<>();
		objects = GLOBAL.model.filter(null, RDF.TYPE, GLOBAL.factory
		.createIRI("http://www.google.com/digitalbuildings/0.0.1/hvac#Fan_ss_coc")).subjects().stream()
		.map(mapper->(IFan_ss_coc)mapper)
		.collect(Collectors.toSet());

		return objects;
	}
}